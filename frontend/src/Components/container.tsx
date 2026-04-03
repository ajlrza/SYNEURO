import type { Component } from 'solid-js';
import { Chatbox } from './chatbox'

export const Container: Component = (props) => {
    
    return (
        //The main container for the characters 

        
        <div id="main-container" class="h-full grid grid-cols-5 border-2 p-10">

            <div id="history-container" class="bg-gradient-to-t from-black to-gray-800 opacity-50 mr-5 pl-5 flex flex-col border-2 p-5 bg-blue-200">
                <h3>History</h3>
                <h4>Conversation 1</h4>
                <h4>Conversation 2</h4>
                <h4>Conversation 3</h4>
            </div>

            {/* The container below will have the background image as the room */}
            <div id="character-container" class="grid grid-cols-3 col-span-4 border-2 p-5">
                
                <img src="./kurisuu.png" class="border-2 size-100 object-cover object-top"/>

                <div id="misc" class="h-fit w-fit flex border-2">
                    <h4>Interactive Items by the Character</h4>
                    
                    <div>Item 1</div>
                    <div>Item 2</div>
                    <div>Item 3</div>
                    <div>Item 4</div>

                    <div>Status 1</div>
                    <div>Status 2</div>
                    <div>Status 3</div>
                </div>

                <Chatbox/>

            </div>

        </div>


        )
    }

