from database import supabase

class AdminRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Admins")
            .select("username, created_at, role, discord_id, reddit_id, email")
            .execute()
        )
        return response.data
    
    @staticmethod
    def create(data: dict):
        return (
            supabase
            .table("Admins")
            .insert(data)
            .execute()
        )
    
    @staticmethod
    def getDataByUsername(username: str):
        return (
            supabase
            .table("Admins")
            .select("username, created_at, role, discord_id, reddit_id, email")
            .eq("username", username)
            .execute()
        ).data
    
    @staticmethod
    def updateData(username: str, data: dict):
        return (
            supabase
            .table("Admins")
            .update(data)
            .eq("username", username)
            .execute()
        )
    
    @staticmethod
    def deleteData(username: str):
        return (
            supabase
            .table("Admins")
            .delete()
            .eq("username", username)
            .execute()
        )
    
    @staticmethod
    def updatePassword(username: str, passwordHash: str):
        return (
            supabase
            .table("Admins")
            .update(
                {"password_hash": passwordHash}
            )
            .eq("username", username)
            .execute()
        )
    
    @staticmethod
    def exists(username: str) -> bool:
        data= (
            supabase
            .table("Admins")
            .select("username")
            .eq("username", username)
            .execute
        )

        if data:
            return True
        else:
            return False
        
    @staticmethod
    def getDataByUsernames(username: str):
        return (
            supabase
            .table("Admins")
            .select("*")
            .eq("username", username)
            .single()
            .execute()
        ).data
    