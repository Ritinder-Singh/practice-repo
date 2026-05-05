// =============================================================================
// PROJECT: Type-Safe Event Emitter (Exclusive)
// =============================================================================
// Roadmap: Exclusive — conditional types + mapped types event emitter
//
// TODO 1: Core TypedEventEmitter<Events extends Record<string, unknown>>
//   on<E extends keyof Events>(event:E, handler:(data:Events[E])=>void): this
//   off / emit / once
//
// TODO 2: Async once() — returns Promise<Events[E]>
//   async function waitFor<Events, E extends keyof Events>(
//     emitter: TypedEventEmitter<Events>, event: E
//   ): Promise<Events[E]>
//
// TODO 3: Wildcard listener
//   onAny(handler: <E extends keyof Events>(event:E, data:Events[E]) => void): this
//
// Usage:
//   interface AppEvents { login:{userId:string}; error:{msg:string} }
//   const e = new TypedEventEmitter<AppEvents>();
//   e.on("login", ({userId}) => ...);  // userId: string — fully typed
// =============================================================================

export class TypedEventEmitter<Events extends Record<string, unknown>> {
  private handlers = new Map<keyof Events, Set<(d: any) => void>>();

  on<E extends keyof Events>(event: E, handler: (data: Events[E]) => void): this {
    // TODO
    return this;
  }
  off<E extends keyof Events>(event: E, handler: (data: Events[E]) => void): this {
    // TODO
    return this;
  }
  emit<E extends keyof Events>(event: E, data: Events[E]): void {
    // TODO
  }
  once<E extends keyof Events>(event: E, handler: (data: Events[E]) => void): this {
    // TODO: wrap handler, auto-remove after first call
    return this;
  }
}
