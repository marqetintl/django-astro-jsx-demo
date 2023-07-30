import { watch } from "fs";
import { spawn } from "child_process";
import { WebSocket, WebSocketServer } from "ws";

const wss = new WebSocketServer({ port: 8080 });

function build(delay = 500) {
  let timer;

  return () => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      const build = spawn("yarn", ["build"], { stdio: "inherit" });

      build.on("exit", () => {
        wss.clients.forEach((client) => {
          if (client.readyState === WebSocket.OPEN) {
            client.send("reload");
          }
        });
      });
    }, delay);
  };
}

const buildDebounced = build();

watch("./src", { recursive: true }, () => {
  console.log("changed");

  buildDebounced();
});

console.log("Dev server started: http://localhost:8080");
