// see: https://www.npmjs.com/package/styled-components
import styled from "styled-components";

export const ContainerLayout = styled.div`
  height: 89vh;
  display: flex;
  flex-direction: row;
`;

export const SidebarLayout = styled.div`
  width: 250px;
  min-height: 700px;
`;

export const ContentLayout = styled.div`
  flex: 1;
`;

export const MenuLayout = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

export const SubMenuLayout = styled.li`
  font-weight: bold;
`;

export const MenuItemLayout = styled.li`
  cursor: pointer;
`;

export const Logo = styled.div`
  border-radius: 5%;
  position: absolute;
  bottom: 10px;
  left: 0;
  right: 0;
  display: block;
  margin: 0 auto;
  width: 90%;
  height: 125px;
  background-image: url("/youtube-banner-image.png");
  background-size: cover;
`;
