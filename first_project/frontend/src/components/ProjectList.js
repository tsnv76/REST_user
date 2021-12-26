import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td><Link to={`/project/${project.id}`}>{project.name} </Link></td>
            <td>{project.repo_link}</td>
            <td>{project.users }</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
            </center>
    )
}

export default ProjectList;