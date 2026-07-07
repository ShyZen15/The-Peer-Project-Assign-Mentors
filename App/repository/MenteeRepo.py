from database import supabase

class MenteeRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Mentees")
            .select("*")
            .execute()
        )
        return response.data

    @staticmethod
    def createData(data: dict):
        return (
            supabase
            .table("Mentees")
            .insert(data)
            .execute()
        )


    @staticmethod
    def getDataByID(id: str):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("discord_id", id)
            .execute()
        ).data

    @staticmethod
    def updateData(id: str, data: dict):
        return (
            supabase
            .table("Mentees")
            .update(data)
            .eq("discord_id", id)
            .execute()
        )

    @staticmethod
    def updateDataField(id: str, data, field: str):
        return (
            supabase
            .table("Mentees")
            .update(
                {field: data}
            )
            .eq("discord_id", id)
            .execute()
        )

    @staticmethod
    def deleteData(id: str):
        return (
            supabase
            .table("Mentees")
            .delete()
            .eq("discord_id", id)
            .execute()
        )

    @staticmethod
    def getCount():
        return len(
            (
                supabase
                .table("Mentees")
                .select("*")
                .execute()
            ).data
        )
    
    @staticmethod
    def getByTrack(track: str):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("track", track)
            .execute()
        ).data
    
    @staticmethod
    def getByAvailability(availability: str):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("availability", availability)
            .execute()
        ).data
    
    @staticmethod
    def getByTrackAndAvailability(track: str, availability: str):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("track", track)
            .eq("availability", availability)
            .execute()
        ).data
    
    @staticmethod
    def getByEmail(email: str):
        return (
            supabase
            .table("Mentees")
            .select("*")
            .eq("email", email)
            .execute()
        ).data