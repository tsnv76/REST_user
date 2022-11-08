import {Link} from 'react-router-dom'

const ProjectItem = ({project, delete_project}) => {
    return(
        <tr>
            <td><Link to={`/project/${project.id}`}>{project.name} </Link></td>
            <td>{project.repo_link}</td>
            <td>{project.users }</td>
            <td><button onClick={()=>delete_project(project.id)} type="button">Delete</button> </td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {
    return (
        <center><table border="1" >
            <th>
                Title
            </th>
            <th>
                Link to repository
            </th>
            <th>
                Users
            </th>
            <th></th>
            {projects.map((project) => <ProjectItem project={project} delete_project={delete_project}/>)}
        </table>
            </center>
    )
}

export default ProjectList;