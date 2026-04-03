import type { Component } from 'solid-js';

export const Chatbox: Component = (props) => {
    return (
        // Responsive Borders: docked to the bottom edges on mobile, fully rounded floating box on desktop
        <div class="flex flex-col w-full max-w-5xl bg-[#0d1117]/85 backdrop-blur-xl border-t border-x md:border-b border-gray-700/50 rounded-t-2xl md:rounded-2xl shadow-[0_-10px_40px_rgba(0,0,0,0.5)] md:shadow-[0_0_40px_rgba(0,0,0,0.5)] overflow-hidden pointer-events-auto ring-1 ring-white/5">

            {/* Chat Area - Heights adapt to leave room for the sprite on mobile */}
            <div class="flex flex-col p-4 md:p-6 h-[40vh] md:h-[35vh] min-h-[250px] overflow-y-auto space-y-5 md:space-y-6">
                
                {/* Character Message */}
                <div class="flex gap-2 md:gap-4 items-end w-full">
                    {/* Responsive Avatar */}
                    <div class="w-8 h-8 md:w-10 md:h-10 rounded-full border border-cyan-500/40 bg-cyan-900/30 flex items-center justify-center shrink-0 shadow-[0_0_10px_rgba(0,255,255,0.15)]">
                        <span class="text-cyan-400 font-bold text-[10px] md:text-xs">MK</span>
                    </div>
                    
                    <div class="flex flex-col items-start w-full">
                        <span class="text-[9px] md:text-[10px] text-cyan-400/80 font-bold mb-1 ml-1 tracking-[0.15em] uppercase">Makise Kurisu</span>
                        <div class="bg-gray-800/80 text-gray-100 rounded-2xl rounded-bl-none px-4 py-3 md:px-5 md:py-3.5 max-w-[90%] md:max-w-[85%] shadow-md border border-gray-700/50 leading-relaxed text-xs md:text-sm backdrop-blur-md">
                            I told you, I'm not your assistant! But... I suppose the responsive layout is highly sophisticated. Are we ready to begin?
                        </div>
                    </div>
                </div>

                {/* User Message */}
                <div class="flex gap-2 md:gap-4 items-end w-full flex-row-reverse">
                    <div class="w-8 h-8 md:w-10 md:h-10 rounded-full border border-purple-500/40 bg-purple-900/30 flex items-center justify-center shrink-0 shadow-[0_0_10px_rgba(168,85,247,0.15)]">
                        <span class="text-purple-400 font-bold text-[10px] md:text-xs">US</span>
                    </div>
                    
                    <div class="flex flex-col items-end w-full">
                        <span class="text-[9px] md:text-[10px] text-purple-400/80 font-bold mb-1 mr-1 tracking-[0.15em] uppercase">You</span>
                        <div class="bg-purple-600/80 text-white rounded-2xl rounded-br-none px-4 py-3 md:px-5 md:py-3.5 max-w-[90%] md:max-w-[85%] shadow-md leading-relaxed text-xs md:text-sm backdrop-blur-md border border-purple-500/50">
                            Looks perfect on my phone now.
                        </div>
                    </div>
                </div>
            </div>

            {/* Input Area - Adjusted for fat thumbs on mobile */}
            <div class="flex items-center p-2 sm:p-3 md:p-4 bg-black/40 border-t border-gray-700/50 gap-2 md:gap-3">
                
                {/* Settings Button - Hidden on very small screens to save space */}
                <button class="hidden sm:block p-2.5 md:p-3 text-gray-400 hover:text-cyan-400 transition-colors bg-gray-800/50 rounded-xl border border-gray-700/50 hover:border-cyan-500/30">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"></path></svg>
                </button>

                {/* Text Input */}
                <input 
                    type="text" 
                    placeholder="Type..." 
                    class="flex-1 bg-gray-900/60 text-gray-100 rounded-xl px-4 py-3 md:py-3.5 outline-none focus:ring-1 focus:ring-cyan-500/50 transition-all border border-gray-700/50 placeholder-gray-500 text-xs md:text-sm shadow-inner min-w-0"
                />
                
                {/* Send Button - Shrinks text to icon on mobile */}
                <button class="bg-cyan-600/90 hover:bg-cyan-500 text-white px-4 md:px-8 py-3 md:py-3.5 rounded-xl font-bold transition-all shadow-[0_0_15px_rgba(0,255,255,0.2)] hover:shadow-[0_0_25px_rgba(0,255,255,0.4)] active:scale-[0.98] flex items-center justify-center gap-2 border border-cyan-400/50 shrink-0">
                    <span class="hidden md:inline text-sm uppercase tracking-widest">Send</span>
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                </button>
            </div>

        </div>
    );
};