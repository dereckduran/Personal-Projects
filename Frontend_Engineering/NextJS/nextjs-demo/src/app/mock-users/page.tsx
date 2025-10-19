import { revalidatePath } from "next/cache";
import { auth, currentUser } from "@clerk/nextjs/server";

type MockUser = {
    id: number;
    name: string;
};

export default async function UsersServer() {

    const authObj = await auth();
    const userObj = await currentUser();

    console.log ({
        authObj,
        userObj,
    });

    const res = await fetch("https://68e150948943bf6bb3c3e68d.mockapi.io/users");
    const users = await res.json();
    
    async function addUser(formData: FormData){
        "use server"
        const name = formData.get("name")
        const res = await fetch("https://68e150948943bf6bb3c3e68d.mockapi.io/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
                /*Authorization: "Bearer <key>" */
            },
            body: JSON.stringify({ name }),  
        }
    );   
    const newUser = await res.json();
    revalidatePath("/mock-users")
    console.log(newUser)
}
    return (
        <div className="py-10">
            <form action = {addUser} className="mb-4">
                <input type="text" name="name" required className="border p-2 mr-2 rounded" />
                <button 
                    type="submit" 
                    className="bg-blue-500 text-whie px-4 rounded"
                >
                    Add user
                </button>
            </form>
        <div className="grid grid-cols-4 gap-4 py-10">
            {users.map((user: MockUser) => (
                <li
                key={user.id}
                className="p-4 bg-white shadow-md rounded-lg text-gray-700"
                >
                    {user.name}
                </li>
            ))}
        </div>
        </div>
    );
}

