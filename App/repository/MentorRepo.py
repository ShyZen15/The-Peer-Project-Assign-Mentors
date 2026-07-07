from database import supabase

class MentorRepo():

    @staticmethod
    def getAll():
        response = (
            supabase
            .table("Mentors")
            .select("*")
            .execute()
        )
        return response.data

    @staticmethod
    def createData(data: dict):
        return (
            supabase
            .table("Mentors")
            .insert(data)
            .execute()
        )


    @staticmethod
    def getDataByID(id: str):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("id", id)
            .execute()
        ).data

    @staticmethod
    def updateData(id: str, data: dict):
        return (
            supabase
            .table("Mentors")
            .update(data)
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def updateDataField(id: str, data, field: str):
        return (
            supabase
            .table("Mentors")
            .update({field: data})
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def deleteData(id: str):
        return (
            supabase
            .table("mentors")
            .delete()
            .eq("id", id)
            .execute()
        )

    @staticmethod
    def getCount():
        return len(
            (
                supabase
                .table("Mentors")
                .select("*")
                .execute()
            ).data
        )
    
    @staticmethod
    def getByTrack(track: str):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("track", track)
            .execute()
        ).data
    
    @staticmethod
    def getByAvailability(availability: str):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("availability", availability)
            .execute()
        ).data
    
    @staticmethod
    def getByTrackAndAvailability(track: str, availability: str):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("track", track)
            .eq("availability", availability)
            .execute()
        ).data
    
    @staticmethod
    def getByEmail(email: str):
        return (
            supabase
            .table("Mentors")
            .select("*")
            .eq("email", email)
            .execute()
        ).data