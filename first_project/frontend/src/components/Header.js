
import React from "react";
import {
Box,
Container,
Row,
Column,
HeaderLink,
Heading,
} from "./HeaderStyle";

const Header = () => {
return (
	<Box>
		<Container>
        <Row>
          <Column>
            <HeaderLink href="#">О компании</HeaderLink>
          </Column>
          <Column>
            <HeaderLink href="#">Услуги</HeaderLink>
          </Column>
          <Column>
            <HeaderLink href="#">Контакты</HeaderLink>
          </Column>
          <Column>
			  <HeaderLink href="#">Соцсети</HeaderLink>
          </Column>
        </Row>
      </Container>
	</Box>
);
};
export default Header;