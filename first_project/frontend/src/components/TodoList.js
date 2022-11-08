const TodoItem = ({todo, delete_todo}) => {
    return(
        <tr>
            <td>{todo.text}</td>
            <td>{todo.created_date}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
            <td><button onClick={()=>delete_todo(todo.id)} type="button">Delete</button> </td>
        </tr>
    )
}

const TodoList = ({todo, delete_todo}) => {
    return (
        <center><table border="1" >
            <th>
                Title
            </th>
            <th>
                Created time
            </th>
            <th>
                Project title
            </th>
            <th>
                User
            </th>
            {todo.map((todo) => <TodoItem todo={todo} delete_todo={delete_todo}/>)}
        </table>
            </center>
    )
}

export default TodoList;