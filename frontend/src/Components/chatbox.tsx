import type { Component } from 'solid-js';

export const Chatbox: Component = (Props) => {
    return (

        // Probably make the main container for the chatbox like, on the
        // level of their waist for mobile, but for desktop make it on the
        // side
        <div id="main-container" class="flex flex-box p-20">

            <div id="conversation-container" class="flex flex-box p-10">
                
                <div id="character-message-container">
                    <div>Makise Kurisu: Hello</div>
                </div>

                <div id="user-message-container">
                    <div>You: Hello</div>
                </div>
   
            </div>

            <div id="input-container" class="flex flex-box p-5">

                <div>Type...</div>

                <div id="input-send-button">
                    
                </div>
            </div>

        </div>
    )
}