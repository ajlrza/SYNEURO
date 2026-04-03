import type { Component } from 'solid-js';

import { Container } from './Components/container';
import { Chatbox } from './Components/chatbox';

const App: Component = () => {
  return (
    <div id="parent-container" class="bg-[url('/background.png')] bg-cover h-screen">
        <Container/>
    </div>

  );
};

export default App;
