from database import supabase
response = (
    supabase
    .table("Mentors")
    .select("*")
    .execute()
)

print(response.data)