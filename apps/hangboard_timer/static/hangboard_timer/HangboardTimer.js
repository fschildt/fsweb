let HangboardTimer = {
    exercise_names: ["Half-Crimp", "3-Finger Drag", "Front 2-Finger Drag", "Middle 2-Finger Drag", "Front 2-Finger Crimp", "Middle 2-Finger Crimp"],
    action_duration: 10,
    pause_duration: 20,
    interval_id: 0,
    start: function() {
        clearInterval(this.interval_id);

        this.el_body = document.body;
        this.el_countdown = document.getElementById("countdown");
        this.el_exercise_state = document.getElementById("exercise_state");
        this.el_exercise_name = document.getElementById("exercise_name");
        if (!this.el_body || !this.el_countdown || !this.el_exercise_state || !this.el_exercise_name || !this.exercise_names.length) {
            console.error("Missing required elements or exercises");
            return;
        }

        this.exercise_index = -1;
        this.is_paused = false;
        this.timer = 0;
        this.last_timestamp = performance.now();

        this.switch_phase();
        this.el_countdown.textContent = Math.ceil(this.timer);
        this.interval_id = setInterval(this.update.bind(this), 100);
    },
    reset: function() {
        this.el_exercise_state.textContent = "";
        this.el_exercise_name.textContent = "";
        this.el_countdown.textContent = "";
        this.el_body.style.backgroundColor = "var(--bg-default)";
        clearInterval(this.interval_id);
        this.interval_id = 0;
    },
    update: function() {
        const current_timestamp = performance.now()
        const elapsed = (current_timestamp - this.last_timestamp) / 1000;
        this.last_timestamp = current_timestamp;

        this.timer -= elapsed;
        if (this.timer <= 0) {
            if (!this.switch_phase()) {
                this.finish();
                return;
            }
        }

        this.el_countdown.textContent = Math.ceil(this.timer);
    },
    switch_phase: function() {
        if (this.is_paused) {
            this.timer = this.action_duration;
            this.is_paused = false;

            this.el_body.style.backgroundColor = "var(--bg-action)";
            this.el_exercise_state.textContent = "Currently:";
        }
        else {
            this.timer = this.pause_duration;
            this.is_paused = true;
            this.exercise_index += 1;
            if (this.exercise_index >= this.exercise_names.length) {
                return false;
            }
            this.el_body.style.backgroundColor = "var(--bg-pause)";
            this.el_exercise_state.textContent = "Upcoming:";
            this.el_exercise_name.textContent = this.exercise_names[this.exercise_index];
        }
        return true;
    },
    finish: function() {
        this.el_exercise.textContent = "";
        this.el_countdown.textContent = "Done.";
        this.el_body.style.backgroundColor = "var(--bg-default)";
        clearInterval(this.interval_id);
        this.interval_id = 0;
    }
}

document.getElementById('btn-start').addEventListener('click', () => HangboardTimer.start());
document.getElementById('btn-reset').addEventListener('click', () => HangboardTimer.reset());
