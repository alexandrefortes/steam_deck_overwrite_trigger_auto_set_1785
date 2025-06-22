# Steam Deck Trigger Calibration Overwrite – Fixed-Value Fork

## Acknowledgements

This fork wouldn't exist without the original work by [kasvtv](https://github.com/kasvtv).  
Huge thanks for creating such a practical and well-documented tool for the Steam Deck community.

If you haven't already, take a look at the original project this fork builds upon: [kasvtv/steam\_deck\_overwrite\_trigger\_cal](https://github.com/kasvtv/steam_deck_overwrite_trigger_cal).

**Fork goal**
Automatically set both trigger **MAX** values on startup. No prompts, no manual input.


Ideal for users who found their Steam Decks ideal values (mine is 1785) using the kasvtv original project method.

I **strongly advise** using the original project first to determine your ideal trigger calibration values: [kasvtv/steam\_deck\_overwrite\_trigger\_cal](https://github.com/kasvtv/steam_deck_overwrite_trigger_cal)

---

## The Problem This Tool Solves

The Steam Deck's analog triggers have a very large deadzone in them. This deadzone is added by the firmware when they are calibrated. It can make games using the analog triggers not feel as nice or responsive. For example, in a racing game, if you want to slightly accelerate or slightly press the brake, during the first few millimeters of pressing the trigger, nothing happens. Only after a considerable distance does the trigger suddenly kick in. This tool can solve that problem by overwriting the calibration values in the firmware. Now you can press that analog trigger just a millimeter and it will start registering.

---

## Warning / Disclaimer

This tool gives you complete control over the calibration values of the Steam Deck's triggers. If you read the instructions carefully and follow them properly, you’ll likely be okay. But if you enter incorrect values, it could make the triggers unresponsive.

In any case, usage is at your own risk. I do not accept liability for any damage that may occur.

---

## Summary of the Fork

After testing the original utility and identifying 1785 as an optimal MAX value for my triggers, I modified the script to:

* Use hardcoded values (1785)
* Remove all prompts
* Run automatically at boot using a systemd service

---

## Quick Usage (Prebuilt Binary)

1. Download `overwrite_trigger_cal` from the [Releases](https://github.com/alexandrefortes/steam_deck_overwrite_trigger_auto_set_1785/releases/tag/v1).
2. Move it to your home folder and make it executable:

   ```bash
   chmod +x ~/overwrite_trigger_cal
   ```
3. Create the systemd service:

   ```bash
   sudo nano /etc/systemd/system/overwrite_trigger_cal.service
   ```

   Paste the following:

   ```ini
   [Unit]
   Description=Steam Deck Trigger Calibration Overwrite
   After=graphical.target

   [Service]
   Type=oneshot
   ExecStart=/home/deck/overwrite_trigger_cal
   RemainAfterExit=true

   [Install]
   WantedBy=multi-user.target
   ```
4. Enable and start the service:

   ```bash
   sudo systemctl enable overwrite_trigger_cal.service
   sudo systemctl start overwrite_trigger_cal.service
   ```

---

## Rebuilding the Binary With Custom Values

If you want to customize the values and rebuild:

### Prerequisites

1. Copy `/usr/bin/trigger_cal` from your Steam Deck to your project folder.
2. Install Docker.

### Steps

1. Clone this repository and edit `src/overwrite_trigger_cal.py`, changing:

   ```python
   lmax = 1785
   rmax = 1785
   ```

2. Build Docker image:

#### Linux/macOS/Windows (PowerShell):

```bash
docker build --progress=plain -t=steam_deck_overwrite_trigger_cal .
```

3. Repack the binary

#### Linux/macOS

```bash
docker run --rm -it \
  -v $(pwd)/src/overwrite_trigger_cal.py:/app/overwrite_trigger_cal.py \
  -v $(pwd)/dist:/app/dist \
  steam_deck_overwrite_trigger_cal
```

#### Windows (PowerShell)

```powershell
docker run --rm -it `
  -v ${PWD}\src\overwrite_trigger_cal.py:/app/overwrite_trigger_cal.py `
  -v ${PWD}\dist:/app/dist `
  steam_deck_overwrite_trigger_cal
```

4. Copy `dist/overwrite_trigger_cal` to your Deck and follow the usage steps above.

### After Resume from Sleep

Currently, this fork does not automatically run after waking from suspend. If you discover a working solution, please [open an issue](https://github.com/alexandrefortes/steam_deck_overwrite_trigger_auto_set_1785/issues) or submit a pull request – I’d love to learn how you did it :)

---

## Disclaimer

* Do **not** redistribute Valve’s `trigger_cal` binary.
* This project only modifies Python code and instructions.
* You assume all risk.

---

## Credits

Fork based on [kasvtv/steam\_deck\_overwrite\_trigger\_cal](https://github.com/kasvtv/steam_deck_overwrite_trigger_cal)

Original license and disclaimers apply.
