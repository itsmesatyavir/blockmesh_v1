const { spawn } = require("child_process");

const process = spawn("node", [".block"]); // Run .block with Node.js
let messageCount = 0;

// High-intensity ANSI colors
const colors = {
    reset: "\x1b[0m",
    red: "\x1b[91m",
    green: "\x1b[92m",
    yellow: "\x1b[93m",
    blue: "\x1b[94m",
    magenta: "\x1b[95m",
    cyan: "\x1b[96m",
    white: "\x1b[97m",
};

process.stdout.on("data", (data) => {
    const output = data.toString().replace(/\{@MeoMunDep x Block Mesh\} - /g, "").trim();

    if (output.includes("Gave")) {
        console.log(colors.green + "GAVE SUCCESSFULL - Please Check You App or Extension" + colors.reset);
    } else if (output.includes("Sent")) {
        console.log(colors.blue + "SENT SUCCESSFULL - Please Wait 10 Minutes || Next Node " + colors.reset);
    } else if (output.length > 0) {
        messageCount++;

        // Show special message for the first 6 messages
        if (messageCount <= 1) {
            console.log(colors.yellow + "\nThis Tool Is Shared By FORESTARMY Developed By MeoMunDep.." + colors.reset);
            console.log(colors.red + "Please Don't Sell This Script" + colors.reset);
            console.log(colors.cyan + "Join Telegram: " + colors.blue + "https://t.me/forestarmy\n" + colors.reset);
        } else {
            console.log(colors.magenta + "Message Received - Keep Connected And Keep Running Node " + colors.reset);
        }
    }

    process.stdout.write(output + "\n");
});

process.stderr.on("data", (data) => {
    console.error(colors.red + "ERROR: " + colors.reset + data.toString().trim());
});

process.on("close", (code) => {
    console.log(colors.white + `Process exited with code ${code}` + colors.reset);
});
