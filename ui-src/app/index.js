/**
 * Created by radwan on 8/25/17.
 */
import ReactDOM from 'react-dom'
import {BrowserRouter} from 'react-router-dom';
import FairuzeApp from "./components/FairuzeApp.jsx";

const renderApp = () => (
  <BrowserRouter>
    <FairuzeApp />
  </BrowserRouter>
);

const root = document.getElementById('fairuzeApp');
ReactDOM.render(renderApp(), root);
