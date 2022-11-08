import {Box, Column, Container, Row} from "./HeaderStyle";
import {Link} from "react-router-dom";
import React from "react";

<nav>
        <Box>
            <Container>
            <Row>
              <Column>
                <Link to="/">Пользователи</Link>
              </Column>
              <Column>
                <Link to="/projects">Проекты</Link>
              </Column>
              <Column>
                <Link to="/todo">Список заданий</Link>
              </Column>
              <Column>
                  {/*<Link to="/login">Login</Link>*/}
                { this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to="/login">Login</Link> }
              </Column>
            </Row>
          </Container>
        </Box>
</nav>