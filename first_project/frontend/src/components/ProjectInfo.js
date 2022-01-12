import {useParams} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>{project.name}</td>
            <td>{project.repo_link}</td>
            <td>{project.users }</td>
        </tr>
    )
}

const ProjectInfo = ({projects}) => {
    let {id} = useParams();
    let filteredProjects = projects.filter((project) => project.users.includes(parseInt(id)))

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
            {filteredProjects.map((project) => <ProjectItem project={project} />)}
        </table>
            </center>
    )
}

export default ProjectInfo;