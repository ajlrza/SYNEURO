import type { Component } from 'solid-js';
import { createEffect, createSignal, on } from 'solid-js';
import { postMessage, testMessage } from './Services/postMessage';

// MAIN APP
const App: Component = () => {
  // Main App Global States
  let [responseChunk, setResponseChunk] = createSignal("");
  let [displayChunk, setDisplayChunk] = createSignal("");
  let [userMessageDisplay, setUserMessageDisplay] = createSignal("");

  // Send message LOGIC
  async function sendMessage(e: SubmitEvent): Promise<void> {
    e.preventDefault();

    const form = e.currentTarget as HTMLFormElement;

    const formData = new FormData(form);
    const user = "Okabe"
    const message = formData.get("userMessage") as string;
    const date = new Date();
    const time = date.getTime();
    const conversation_id = 1;

    // We must check either the conversation already has an ID or not

    await testMessage(message);

    form.reset();
    
    const kurisuMessage: Response | undefined = await postMessage(user, message, date, time, conversation_id);
    if (kurisuMessage == undefined) {
       const messageRetry: Response | undefined = await postMessage(user, message, date, time, conversation_id);
    }
    if (kurisuMessage != undefined) {
        decodeMessage(kurisuMessage);
        setUserMessageDisplay(message);
    }
  }

  // Decode the message's byte array LOGIC
  async function decodeMessage(kurisuMessage: Response | undefined): Promise<void> {

    if (!kurisuMessage || !kurisuMessage.body) {
        return undefined; 
      }

    if (kurisuMessage != undefined) {
        const kurisuReadMessageStream = kurisuMessage.body?.getReader();
        const streamDecoder = new TextDecoder();
        let cleanedText;

        while (true) {
          let {done, value}: any = await kurisuReadMessageStream?.read()
          let text = streamDecoder.decode(value)
          const cleanedText = text
          .replace(/\n+/g, ' ') 
          .replace(/\s{2,}/g, ' ') 
          .trim();
          setResponseChunk((prev) => prev.replace(/\n/g, "") + cleanedText)
          displayChunkFunction(responseChunk())
          if (done == true) {
            break;
            }
          }
        }
      }

    // Typewriter effect LOGIC
    async function delay(ms: number): Promise<void> {
      return new Promise((resolve) => {
        setTimeout(resolve, ms)
      })
    }
    
    // Display delayed messages as chunk for typewriter effect LOGIC
    async function displayChunkFunction(kurisuMessage: String) {
      let chunkDisplay = ""

      for (const word of kurisuMessage.split(" ")) {
          chunkDisplay = chunkDisplay + " " + word
          await delay(20);
          setDisplayChunk(chunkDisplay)
      }
    }


  return (
    // h-[100dvh] ensures it fits exactly to the mobile browser's visible viewport
    <div class="flex h-[100dvh] w-full bg-[#0a0a0c] bg-[url('/background.png')] bg-cover bg-center overflow-hidden font-sans text-gray-100 select-none pb-[env(safe-area-inset-bottom)]">
    
    {/* Subtly transparent Sidebar (ChatGPT / Gemini style) */}
    <div class="hidden md:flex flex-col w-64 lg:w-72 h-full bg-black/80 border-r border-gray-800/60 backdrop-blur-md z-40 relative shadow-[4px_0_24px_rgba(0,0,0,0.5)]">
      
      {/* Sidebar Top: New Chat / Action Button */}
      <div class="p-4">
        <button class="flex items-center gap-3 w-full px-4 py-3 bg-gray-800/40 hover:bg-gray-700/60 text-white rounded-lg transition-all border border-gray-700/50 text-sm font-medium group">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-cyan-400 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
          </svg>
          <span class="tracking-wide">New Timeline</span>
        </button>
      </div>

      {/* Sidebar Middle: Chat History / Saved States */}
      <div class="flex-1 overflow-y-auto px-3 py-2 scrollbar scrollbar-thumb-gray-700 scrollbar-track-transparent">
        <h4 class="text-[10px] font-black text-gray-500 uppercase tracking-[0.2em] mb-3 px-2">Memory Logs</h4>
        
        <ul class="flex flex-col gap-1 text-sm text-gray-300">
          <li class="px-3 py-2.5 rounded-md bg-gray-800/70 text-cyan-400 font-medium cursor-pointer truncate border-l-2 border-cyan-400 shadow-sm">
            Current Timeline: 1.048596
          </li>
          <li class="px-3 py-2.5 rounded-md hover:bg-gray-800/40 cursor-pointer truncate transition-colors">
            Amadeus System Init
          </li>
          <li class="px-3 py-2.5 rounded-md hover:bg-gray-800/40 cursor-pointer truncate transition-colors">
            Time Machine Theory
          </li>
          <li class="px-3 py-2.5 rounded-md hover:bg-gray-800/40 cursor-pointer truncate transition-colors text-gray-500 italic">
            D-Mail Experiment #04
          </li>
        </ul>
      </div>

      {/* Sidebar Bottom: User / Settings */}
      <div class="p-4 border-t border-gray-800/60 bg-black/20">
        <button class="flex items-center gap-3 w-full p-2 hover:bg-gray-800/50 rounded-lg transition-colors text-left group">
          <div class="w-9 h-9 rounded-full bg-cyan-950 border border-cyan-500/50 flex items-center justify-center text-cyan-400 font-bold text-sm shadow-[0_0_10px_rgba(6,182,212,0.2)]">
            U
          </div>
          <div class="flex-1 overflow-hidden">
            <div class="text-sm text-gray-200 font-medium truncate group-hover:text-white transition-colors">Hououin Kyouma</div>
            <div class="text-[10px] text-gray-500 uppercase tracking-widest truncate">Lab Mem 001</div>
          </div>
          <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
          </svg>
        </button>
      </div>
    </div>

    {/* Main Content Area */}
    <main class="relative flex-1 flex flex-col h-full overflow-hidden">
      
      {/* Subtle CRT/Scanline effect overlay (Moved to main so it overlays VN content, not sidebar) */}
      <div class="absolute inset-0 pointer-events-none bg-[linear-gradient(rgba(18,16,16,0)_50%,rgba(0,0,0,0.25)_50%)] bg-[length:100%_4px] z-10 opacity-30"></div>

      {/* Top Left VN HUD */}
      <div class="absolute top-safe pt-2 pl-2 sm:top-6 sm:left-6 z-20 flex items-center bg-black/50 border border-gray-400/30 px-2 sm:px-4 py-1 sm:py-1.5 shadow-lg backdrop-blur-sm scale-90 sm:scale-100 origin-top-left">
        <div class="flex items-center gap-2 sm:gap-4 text-white font-mono tracking-widest text-base sm:text-xl">
          <span>8 / 1</span>
          <span class="text-xs sm:text-sm tracking-normal">(SUN)</span>
          
          <div class="flex items-center gap-1.5 sm:gap-2 ml-2 sm:ml-4 opacity-80">
            <svg class="w-3 h-3 sm:w-4 sm:h-4" fill="currentColor" viewBox="0 0 20 20">
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
            </svg>
            <div class="flex gap-[2px] h-2.5 sm:h-3 items-end">
              <div class="w-[3px] h-1.5 bg-white"></div>
              <div class="w-[3px] h-2 bg-white"></div>
              <div class="w-[3px] h-full bg-white"></div>
            </div>
          </div>
        </div>
      </div>

      {/* Character Sprite */}
      <div class="absolute inset-x-0 top-[5vh] sm:top-[8vh] pointer-events-none z-0 flex justify-center items-start">
        <img 
          src="./kurisu.png" 
          alt="Makise Kurisu" 
          class="h-[110dvh] sm:h-[130dvh] lg:h-[150dvh] w-auto max-w-none object-contain object-top drop-shadow-[0_0_20px_rgba(0,0,0,0.8)] transition-all duration-300"
        />
      </div>

      {/* Visual Novel Dialogue Box Area */}
      <div id="chatBox" class="absolute bottom-0 left-0 right-0 z-30 flex flex-col bg-gradient-to-t from-black via-black/95 to-transparent pt-32 pb-6 px-6">
        
        <div class="flex flex-col gap-8 max-w-4xl w-full mx-auto mb-10 overflow-y-auto max-h-[80vh] scrollbar scrollbar-thumb-cyan-400 scrollbar-track-gray-800">
          
          <div class="flex flex-col self-start max-w-[85%] animate-fade-in">
            <h3 class="text-cyan-400 text-xs md:text-sm font-black mb-2 tracking-[0.3em] uppercase border-l-2 border-cyan-400 pl-3">
              Makise Kurisu
            </h3>

            {/*Previous Messages */}
            <div class="text-lg md:text-2xl lg:text-3xl text-white font-medium drop-shadow-[0_2px_10px_rgba(0,0,0,1)] leading-relaxed">
              {displayChunk()}
            </div>

            {/*Current Message */}
            <div id="kurisuDisplayChunk" class="text-lg md:text-2xl lg:text-3xl text-white font-medium drop-shadow-[0_2px_10px_rgba(0,0,0,1)] leading-relaxed">
              {displayChunk()}
            </div>
          </div>

          <div class="flex flex-col self-end text-right max-w-[75%] animate-fade-in">
            <h3 class="text-gray-500 text-xs md:text-sm font-black mb-2 tracking-[0.3em] uppercase pr-3 border-r-2 border-gray-700">
              You
            </h3>

            {/*Previous Messages */}            
            <div class="text-base md:text-xl text-gray-300 italic font-medium drop-shadow-lg leading-snug">
              {userMessageDisplay()}
            </div>

            {/*Current Message */}
            <div id="userDisplayChunk" class="text-base md:text-xl text-gray-300 italic font-medium drop-shadow-lg leading-snug">
              {userMessageDisplay()}
            </div>
          </div>
        </div>

        <form
          onSubmit={(e) => sendMessage(e)} 
          class="flex items-center gap-4 border-b border-white/20 pb-2 focus-within:border-cyan-500/50 transition-all max-w-4xl mx-auto w-full group"
        >
          <input 
            type="text" 
            name="userMessage"
            placeholder="Type your response..." 
            class="flex-1 bg-transparent text-gray-100 outline-none placeholder-gray-700 text-lg py-2"
          />
          <button type="submit" class="text-gray-500 group-focus-within:text-cyan-400 hover:text-cyan-300 transition-colors uppercase text-sm font-black tracking-widest flex items-center gap-2">
            <span>Send</span>
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M14 5l7 7m0 0l-7 7m7-7H3" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </form>

        <div class="mt-6 flex justify-between items-center max-w-4xl mx-auto w-full text-[10px] text-gray-600 font-bold tracking-widest uppercase">
          <div class="flex gap-6">
            <button class="hover:text-white transition-colors">Change</button>
            <button class="hover:text-white transition-colors">Interact</button>
          </div>
          <div class="flex gap-6">
            <button class="hover:text-white transition-colors md:hidden">History</button>
            <button class="hover:text-white transition-colors md:hidden">Settings</button>
          </div>
        </div>
      </div>
    </main>
  </div>
  );
};

export default App;