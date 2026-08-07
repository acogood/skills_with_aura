import { Composition } from "remotion";
import { Demo, DEMO_DURATION, DEMO_FPS, DEMO_HEIGHT, DEMO_SIZE } from "./Demo";

export const RemotionRoot = () => (
  <Composition
    id="Demo"
    component={Demo}
    fps={DEMO_FPS}
    durationInFrames={DEMO_DURATION}
    width={DEMO_SIZE}
    height={DEMO_HEIGHT}
  />
);
