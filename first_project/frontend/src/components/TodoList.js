const TodoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.text}</td>
            <td>{todo.created_date}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const TodoList = ({todo}) => {
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
            {todo.map((todo) => <TodoItem todo={todo} />)}
        </table>
            </center>
    )
}

export default TodoList;