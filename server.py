from mcp.server.fastmcp import FastMCP
from gmail_client import get_gmail_service, search_application_emails
from db import init_db, save_application

mcp = FastMCP("Job Application Tracker")

@mcp.tool()
def scan_application_emails(query: str = "thank you for applying"):
    """
    Scan Gmail for job application confirmation emails
    """
    service = get_gmail_service()
    messages = search_application_emails(service, query)

    count = 0
    for msg in messages:
        # For MVP, we just store email ID
        save_application(
            company="UNKNOWN",
            role="UNKNOWN",
            date="UNKNOWN",
            source="Gmail",
            email_id=msg["id"]
        )
        count += 1

    return f"Imported {count} emails"

if __name__ == "__main__":
    init_db()
    mcp.run()
