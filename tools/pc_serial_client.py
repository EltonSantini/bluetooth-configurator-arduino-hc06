import argparse
import time

try:
    import serial
except ImportError:
    serial = None


def main():
    parser = argparse.ArgumentParser(description="PC serial client for Arduino HC-06 configurator.")
    parser.add_argument("--port", required=True, help="Serial port, e.g. COM5 or /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=9600, help="Baud rate (default: 9600)")
    args = parser.parse_args()

    if serial is None:
        print("pyserial is not installed. Run: pip install pyserial")
        return

    with serial.Serial(args.port, args.baud, timeout=1) as ser:
        print(f"Connected to {args.port} at {args.baud} baud.")
        print("Type lines to send to Arduino. Ctrl+C to exit.\n")

        try:
            while True:
                if ser.in_waiting:
                    data = ser.read(ser.in_waiting)
                    print(data.decode(errors="ignore"), end="")

                user_input = input("")
                ser.write(user_input.encode() + b"\n")
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\nExiting.")


if __name__ == "__main__":
    main()
