let React = require('react');
let ReactDOM = require('react-dom');
import './scripts/sidebar.js';


class Feed extends React.Component {
    render() {
        return (
            <div>
                <h1>Feed mascotas</h1>
            </div>
        );
    }
}

ReactDOM.render(
    <Feed/>,
    document.getElementById('feed-root')
);