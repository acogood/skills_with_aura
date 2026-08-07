import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";

export const DEMO_FPS = 20;
export const DEMO_SIZE = 960;
export const DEMO_HEIGHT = 810;
export const DEMO_DURATION = 310;

const FONT =
  "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif";

const AUTHOR = "Mina Park";

type Line = { text: string; bullet?: boolean };
type Section = { color: string; label: string; lines: Line[] };

const SECTIONS: Section[] = [
  {
    color: "#0a66c2",
    label: "hook",
    lines: [
      { text: "The best channels now cost $50, not a budget." },
      {
        text: "Most marketers still budget like it's 2015. The scrappy ones already moved.",
      },
    ],
  },
  {
    color: "#d97706",
    label: "old way vs new way",
    lines: [
      { text: "Old way: save up, buy ads, rent attention until the money runs out." },
      { text: "New way: spend $50 to see who spreads your thing for free." },
      {
        bullet: true,
        text: "Gymshark started with £1,000 and a garage, mailing free shirts to the fitness YouTubers its founder already watched. That seeding became the channel. One expo drop later: £30,000 in 30 minutes. The brand is now worth over £1B.",
      },
      {
        bullet: true,
        text: "Cal AI launched in 2024 with no ad budget. The first move was cheap TikToks and small creator partnerships. That one channel compounded to roughly $30M a year, all bootstrapped.",
      },
    ],
  },
  {
    color: "#059669",
    label: "everyday analogy",
    lines: [
      {
        text: "You already do this as a buyer. You skip the menu description and go straight to the photos and the reviews, because seeing the thing convinces you in a way that a description never does.",
      },
    ],
  },
  {
    color: "#7c3aed",
    label: "the flip",
    lines: [
      {
        text: "So flip the order. Run one cheap test first, then put real money behind whatever actually spreads.",
      },
    ],
  },
  {
    color: "#dc2626",
    label: "first-person proof",
    lines: [
      {
        text: "I ran my own version with $50 on a meme page. It made $2,000 the first month and still does about $1,000 a month a year later, and I've barely touched it.",
      },
    ],
  },
  {
    color: "#0d9488",
    label: "open question CTA",
    lines: [
      {
        text: "Where are you still saving for a big campaign when $50 would tell you the truth faster?",
      },
    ],
  },
];

const PASTE_START = 16;
const PASTE_GAP = 5;
const BREAK_START = 64;
const STEP_GAP = 34;
const CAPTION_AT = 272;

const ramp = (frame: number, from: number, span: number) =>
  interpolate(frame, [from, from + span], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

const Chunk: React.FC<{ at: number; children: React.ReactNode }> = ({
  at,
  children,
}) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        opacity: ramp(frame, at, 4),
        transform: `translateY(${interpolate(ramp(frame, at, 4), [0, 1], [6, 0])}px)`,
      }}
    >
      {children}
    </div>
  );
};

const Highlight: React.FC<{
  at: number;
  dimAt: number | null;
  color: string;
  label: string;
}> = ({ at, dimAt, color, label }) => {
  const frame = useCurrentFrame();
  const on = ramp(frame, at, 6);
  const dim = dimAt === null ? 0 : ramp(frame, dimAt, 6);
  const borderOpacity = on * (1 - 0.6 * dim);
  const chipOn = ramp(frame, at + 5, 5);
  return (
    <>
      <div
        style={{
          position: "absolute",
          inset: "-7px -10px",
          border: `2.5px solid ${color}`,
          borderRadius: 10,
          opacity: borderOpacity,
          transform: `scale(${interpolate(on, [0, 1], [0.985, 1])})`,
        }}
      />
      <div
        style={{
          position: "absolute",
          top: -7,
          left: 10,
          transform: `translateY(-50%) scale(${interpolate(chipOn, [0, 1], [0.8, 1])})`,
          opacity: chipOn,
          background: color,
          color: "#fff",
          fontFamily: FONT,
          fontSize: 15,
          fontWeight: 600,
          lineHeight: "22px",
          padding: "1px 10px",
          borderRadius: 11,
          whiteSpace: "nowrap",
        }}
      >
        {label}
      </div>
    </>
  );
};

const Icon: React.FC<{ d: React.ReactNode; size?: number }> = ({
  d,
  size = 24,
}) => (
  <svg
    width={size}
    height={size}
    viewBox="0 0 24 24"
    fill="none"
    stroke="#56544f"
    strokeWidth={1.8}
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    {d}
  </svg>
);

export const Demo: React.FC = () => {
  const frame = useCurrentFrame();

  const dialogIn = ramp(frame, 0, 8);
  const placeholderGone = ramp(frame, PASTE_START - 2, 4);
  const captionOn = ramp(frame, CAPTION_AT, 8);
  const postOn = ramp(frame, CAPTION_AT, 8);

  return (
    <AbsoluteFill style={{ background: "#e6e4df", fontFamily: FONT }}>
      <div
        style={{
          position: "absolute",
          left: 60,
          top: 34,
          width: 840,
          background: "#f7f6f3",
          borderRadius: 14,
          boxShadow: "0 12px 40px rgba(0,0,0,0.28)",
          opacity: dialogIn,
          transform: `scale(${interpolate(dialogIn, [0, 1], [0.96, 1])})`,
          display: "flex",
          flexDirection: "column",
        }}
      >
        {/* header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            padding: "26px 30px 0",
          }}
        >
          <Img
            src={staticFile("avatar.jpg")}
            style={{
              width: 58,
              height: 58,
              borderRadius: "50%",
              objectFit: "cover",
            }}
          />
          <div style={{ marginLeft: 14 }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                color: "#191817",
                fontSize: 21,
                fontWeight: 700,
              }}
            >
              {AUTHOR}
              <svg width={16} height={16} viewBox="0 0 16 16" style={{ marginLeft: 8 }}>
                <path d="M4 6l4 4 4-4" fill="none" stroke="#56544f" strokeWidth={1.8} />
              </svg>
            </div>
            <div style={{ color: "#56544f", fontSize: 15, marginTop: 2 }}>
              Post to Anyone
            </div>
          </div>
          <div style={{ marginLeft: "auto" }}>
            <Icon
              d={
                <>
                  <path d="M6 6l12 12" />
                  <path d="M18 6L6 18" />
                </>
              }
            />
          </div>
        </div>

        {/* body */}
        <div style={{ padding: "26px 48px 10px", position: "relative" }}>
          <div
            style={{
              position: "absolute",
              top: 26,
              left: 48,
              color: "#8b8880",
              fontSize: 21,
              opacity: 1 - placeholderGone,
            }}
          >
            What do you want to talk about?
          </div>
          {SECTIONS.map((s, i) => (
            <div
              key={i}
              style={{ position: "relative", marginTop: i === 0 ? 24 : 15 }}
            >
              <Chunk at={PASTE_START + i * PASTE_GAP}>
                {s.lines.map((l, j) => (
                  <div
                    key={j}
                    style={{
                      color: "#191817",
                      fontSize: 15.5,
                      lineHeight: 1.5,
                      marginBottom: j < s.lines.length - 1 ? 8 : 0,
                      paddingLeft: l.bullet ? 18 : 0,
                      position: "relative",
                    }}
                  >
                    {l.bullet && (
                      <span
                        style={{
                          position: "absolute",
                          left: 4,
                          top: 0,
                          color: "#191817",
                        }}
                      >
                        •
                      </span>
                    )}
                    {l.text}
                  </div>
                ))}
              </Chunk>
              <Highlight
                at={BREAK_START + i * STEP_GAP}
                dimAt={i < SECTIONS.length - 1 ? BREAK_START + (i + 1) * STEP_GAP : null}
                color={s.color}
                label={s.label}
              />
            </div>
          ))}
        </div>

        {/* icon row */}
        <div
          style={{
            display: "flex",
            gap: 26,
            padding: "18px 30px 20px",
            alignItems: "center",
          }}
        >
          <Icon
            d={
              <>
                <circle cx={12} cy={12} r={9} />
                <path d="M8.5 14a4.5 4.5 0 0 0 7 0" />
                <circle cx={9} cy={10} r={0.6} fill="#56544f" />
                <circle cx={15} cy={10} r={0.6} fill="#56544f" />
              </>
            }
          />
          <Icon
            d={
              <>
                <rect x={3} y={4} width={18} height={16} rx={2} />
                <circle cx={9} cy={10} r={1.6} />
                <path d="M3 17l6-5 4 3 4-4 4 4" />
              </>
            }
          />
          <Icon
            d={
              <>
                <rect x={3} y={5} width={18} height={16} rx={2} />
                <path d="M3 9h18M8 3v4M16 3v4" />
              </>
            }
          />
          <Icon
            d={
              <path d="M12 3l2.2 2.2 3-.6.6 3L21 9.8l-1.6 2.7 1.6 2.7-3.2 1.2-.6 3-3-.6L12 21l-2.2-2.2-3 .6-.6-3L3 15.2l1.6-2.7L3 9.8l3.2-1.2.6-3 3 .6z" />
            }
          />
          <Icon
            d={
              <>
                <path d="M12 5v14M5 12h14" />
              </>
            }
          />
        </div>

        {/* footer */}
        <div
          style={{
            borderTop: "1px solid #ddd9d2",
            display: "flex",
            alignItems: "center",
            justifyContent: "flex-end",
            gap: 18,
            padding: "14px 30px",
          }}
        >
          <Icon
            d={
              <>
                <circle cx={12} cy={12} r={9} />
                <path d="M12 7v5l3 2" />
              </>
            }
          />
          <div style={{ position: "relative", width: 84, height: 40 }}>
            <div
              style={{
                position: "absolute",
                inset: 0,
                borderRadius: 20,
                background: "#e5e3de",
                color: "#a3a09a",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 17,
                fontWeight: 700,
              }}
            >
              Post
            </div>
            <div
              style={{
                position: "absolute",
                inset: 0,
                borderRadius: 20,
                background: "#0a66c2",
                color: "#fff",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontSize: 17,
                fontWeight: 700,
                opacity: postOn,
              }}
            >
              Post
            </div>
          </div>
        </div>
      </div>

      {/* closing caption */}
      <div
        style={{
          position: "absolute",
          bottom: 14,
          left: 0,
          right: 0,
          textAlign: "center",
          color: "#6b6862",
          fontSize: 17,
          opacity: captionOn,
        }}
      >
        drafted by linkedin-post-writer on the “Old Way vs New Way” template
      </div>
    </AbsoluteFill>
  );
};
