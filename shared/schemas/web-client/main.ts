import {dbConfig} from './client-db_interface';
import {infraConfig} from './infra_interface';

const ws = new WebSocket("ws://localhost:8000/ws");
ws.binaryType = "arraybuffer";

export class Syneuro {
    protected dbAPIKey: string;
    protected appMode: string;

    constructor(dbConfig: dbConfig, infraConfig: infraConfig) {
        this.dbAPIKey = dbConfig.apiKey;
        this.appMode = infraConfig.appMode;
    }


}

export class ApplyModel<Object>{
    protected modelName: string;
    protected Syneuro: Syneuro;
    
    constructor(Syneuro: Syneuro) {
        this.Syneuro = Syneuro;
        // Google APIs Node.js Client to search for model name or
        // Have a list of models that can be used and mapping modelName to that
        this.modelName = ""; // temp
    }

}

export class UserWebcam<T> {
    protected userStream: Promise<MediaStream>;

    constructor() {
        this.userStream = navigator.mediaDevices.getDisplayMedia();
    }

    async initiateCam(constraint: MediaStreamConstraints /* { audio: true } or { video: true } or both */) {
        try {
            this.userStream = navigator.mediaDevices.getUserMedia(constraint);
            const stream = await this.userStream;
            /* use the stream */
            /* ineed the matrices */
        } catch (err) {
            /* handle the error */
        }
    }
}