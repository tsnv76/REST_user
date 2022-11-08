const UserItem = ({user}) => {
    return(
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.date_joined}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <center><table border="1" >
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Email
            </th>
            <th>
                Date joined
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
            </center>
    )
}

export default UserList;