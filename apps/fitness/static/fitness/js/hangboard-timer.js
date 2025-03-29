let HangboardTimer = {
    exercise_names: ["Half-Crimp", "3-Finger Drag", "Front 2-Finger Drag", "Middle 2-Finger Drag", "Front 2-Finger Crimp", "Middle 2-Finger Crimp"],
    exercise_reps: [6, 6, 2, 2, 2, 2],
    action_duration: 10,
    pause_duration: 20,
    start: function() {
        this.el_body = document.body;
        this.el_countdown = document.getElementById("countdown");
        this.el_exercise_state = document.getElementById("exercise_state");
        this.el_exercise_name = document.getElementById("exercise_name");
        if (!this.el_body || !this.el_countdown || !this.el_exercise_state || !this.el_exercise_name || !this.exercise_names.length) {
            console.error("Missing required elements or exercises");
            return;
        }
        this.audioContext = this.audioContext || new (window.AudioContext || window.webkitAudioContext)();

        this.reset();
        this.show_state();

        this.interval_id = setInterval(this.update.bind(this), 100);
    },
    reset: function() {
        clearInterval(this.interval_id);
        this.interval_id = 0;
        this.exercise_index = 0;
        this.exercise_rep = 1;
        this.is_paused = true;
        this.timer = this.pause_duration;
        this.last_timestamp = performance.now();
        this.el_body.style.backgroundColor = "var(--bg-default)";
        this.el_countdown.textContent = "";
        this.el_exercise_state.textContent = "";
        this.el_exercise_name.textContent = "";
    },
    update: function() {
        const current_timestamp = performance.now()
        const elapsed = (current_timestamp - this.last_timestamp) / 1000;

        this.last_timestamp = current_timestamp;
        this.timer -= elapsed;

        if (this.timer <= 3 && !this.beep_triggered) {
            this.play_beeps();
            this.beep_triggered = true;
        }
        if (this.timer <= 0) {
            const phase_switched = this.switch_phase();
            if (!phase_switched) {
                this.finish();
                return;
            }
        }

        this.show_state();
    },
    switch_phase: function() {
        if (this.is_paused) {
            this.timer = this.action_duration;
            this.is_paused = false;
        }
        else {
            this.timer = this.pause_duration;
            this.is_paused = true;
            if (this.exercise_rep == this.exercise_reps[this.exercise_index]) {
                this.exercise_index += 1;
                this.exercise_rep = 1;
                if (this.exercise_index >= this.exercise_names.length) {
                    return false;
                }
            }
            else {
                this.exercise_rep += 1;
            }
        }
        this.beep_triggered = false;
        return true;
    },
    show_state: function() {
        this.el_countdown.textContent = Math.ceil(this.timer);
        if (this.is_paused) {
            this.el_body.style.backgroundColor = "var(--bg-pause)";
            this.el_exercise_state.textContent = "Upcoming:";
        }
        else {
            this.el_body.style.backgroundColor = "var(--bg-action)";
            this.el_exercise_state.textContent = "Currently:";
        }
        const name = this.exercise_names[this.exercise_index];
        const rep = this.exercise_rep;
        const reps = this.exercise_reps[this.exercise_index];
        this.el_exercise_name.textContent = `${name} (${rep}/${reps})`;
    },
    play_beeps: function() {
        const now = this.audioContext.currentTime;
        const oscillator = this.audioContext.createOscillator();
        const gain_node = this.audioContext.createGain();
        oscillator.connect(gain_node);
        gain_node.connect(this.audioContext.destination);

        oscillator.type = 'sine';
        oscillator.frequency.value = 400;
        oscillator.frequency.setValueAtTime(500, now + 3.0);

        oscillator.start(now);
        gain_node.gain.setValueAtTime(0.5, now);
        gain_node.gain.setValueAtTime(0, now + 0.5);
        gain_node.gain.setValueAtTime(0.5, now + 1.0);
        gain_node.gain.setValueAtTime(0, now + 1.5);
        gain_node.gain.setValueAtTime(0.5, now + 2.0);
        gain_node.gain.setValueAtTime(0, now + 2.5);
        gain_node.gain.setValueAtTime(0.5, now + 3.0);
        gain_node.gain.setValueAtTime(0, now + 3.5);
        oscillator.stop(now + 3.5);
    },
    finish: function() {
        this.el_exercise_state.textContent = "";
        this.el_exercise_name.textContent = "";
        this.el_countdown.textContent = "Done.";
        this.el_body.style.backgroundColor = "var(--bg-default)";
        clearInterval(this.interval_id);
        this.interval_id = 0;
    }
}

document.getElementById('btn-start').addEventListener('click', () => HangboardTimer.start());
document.getElementById('btn-reset').addEventListener('click', () => HangboardTimer.reset());
