class DigitalClock {
    constructor(element) {
        this.element = element;
    }

    start () {
        setInterval(() => {
            this.update();
        }, 500)

    }

    update() {
        const parts = this.getTimeParts();
        const minuteFormatted = parts.min.toString().padStart(2, "0");
        const timeFormatted = `${parts.hour}:${minuteFormatted}`;
        const amPm = parts.isAm ? "AM" : "PM";
        this.element.querySelector(".clock-time").textContent = timeFormatted;
        this.element.querySelector(".clock-ampm").textContent = amPm;
    }
    
    getTimeParts() {
        const now = new Date();

        return {
            hour: now.getHours() % 12 || 12,
            min: now.getMinutes(),
            isAm: now.getHours() < 12
        }
    }
}

// going to select the first element with a class of clock

const clockElement = document.querySelector(".clock");
const clockObject = new DigitalClock(clockElement)

console.log(clockObject.getTimeParts());
clockObject.start();