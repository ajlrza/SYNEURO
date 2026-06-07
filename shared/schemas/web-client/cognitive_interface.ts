export interface SyneuroAffectiveState {
  salienceScore: number;
  limbicValence: number;
  activeNetwork: 'CEN' | 'DFM' | 'VEN';
}

export interface SyneuroInferencePayload {
  messageId: string;
  tokens: string[];
  affectiveState: SyneuroAffectiveState;
  timestamp: number;
}