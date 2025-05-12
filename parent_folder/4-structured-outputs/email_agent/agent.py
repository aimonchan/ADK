from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email.")
    body:str = Field(description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )

# --- Create Email Generator Agent ---
root_agent = LlmAgent(
    name="email_agent",
    model= "gemini-2.0-flash",
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line(concise and relevant)
        - Write a well-structured email body with:
            - A polite greeting
            - Clear and concise main content
            - Appropriate closing
            - Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        Do NOT include any additional text or explanations outside of the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)


# #For generating blog posts:
# class BlogPostContent(BaseModel):
#     title: str = Field(description="The title of the blog post.")
#     content: str = Field(description="The main content of the blog post. Should be well-structured with proper paragraphs, headings, and formatting.")
#     tags: list[str] = Field(description="A list of relevant tags for the blog post.")

#For generating meeting agendas:
# class MeetingAgenda(BaseModel):
#     title: str = Field(description="The title of the meeting.")
#     date: str = Field(description="The date of the meeting (YYYY-MM-DD).")
#     time: str = Field(description="The time of the meeting (HH:MM).")
#     location: str = Field(description="The location of the meeting.")
#     topics: list[str] = Field(description="A list of topics to be discussed during the meeting.")

#For generating social media posts:
# class SocialMediaPost(BaseModel):
#     platform: str = Field(description="The social media platform (e.g., Twitter, Facebook, Instagram).")
#     text: str = Field(description="The text content of the social media post.")
#     image_url: str = Field(description="URL of the image to be included in the post (optional).")
#     hashtags: list[str] = Field(description="A list of relevant hashtags for the post.")