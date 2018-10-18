# Helper functions


def h(elm_type, props='', *args):
    return React.createElement(elm_type, props, *args)


def render(react_element, destination_id, callback=lambda: None):
    container = document.getElementById(destination_id)
    ReactDOM.render(react_element, container, callback)


# Create a component


class Hello(object, React.Component):
    def __init__(self):
        self.state = {'counter': 0}

    def render(self):
        return h('div', { 'className': 'maindiv' },
            h('h1', None, 'Hello ', self.props['name']),
            h('p', None, 'Lorem ipsum dolor sit amet.'),
            h('p', None, 'Counter: ', self.state['counter'])
        )

    def updateCounter(self):
        self.setState({ 'counter': self.state['counter'] + 1 })

    def componentDidMount(self):
        setInterval(self.updateCounter, 1000)


# Render the component in a 'container' div

element = React.createElement(Hello, {'name': 'React!'})
render(element, 'container')
