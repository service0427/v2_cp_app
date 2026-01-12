import sys
import time
import subprocess
import argparse

def main():
    # 1. Parse Loop/Delay arguments, keep the rest for run.py
    parser = argparse.ArgumentParser(description="Batch Loop Wrapper for run.py")
    parser.add_argument("--loop", type=int, default=1, help="Number of iterations (-1 for infinite)")
    parser.add_argument("--delay", type=float, default=5.0, help="Delay in seconds between iterations")
    
    # parse_known_args allows us to capture the rest easily
    args, unknown_args = parser.parse_known_args()
    
    loop_count = args.loop
    delay = args.delay
    
    print(f"[Loop] Starting Batch Execution")
    print(f"[Loop] Iterations: {loop_count if loop_count != -1 else 'Infinite'}")
    print(f"[Loop] Delay: {delay}s")
    print(f"[Loop] Arguments passed to run.py: {' '.join(unknown_args)}")
    print("="*60)
    
    iteration = 0
    try:
        while True:
            if loop_count != -1 and iteration >= loop_count:
                print(f"\n[Loop] Completed {loop_count} iterations.")
                break
                
            iteration += 1
            print(f"\n[Loop] >>> Iteration {iteration} / {loop_count if loop_count != -1 else '∞'}")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Loop] Start Time: {timestamp}")
            
            # 2. Execute run.py using subprocess
            cmd = [sys.executable, "run.py"] + unknown_args
            
            try:
                # We want to wait for it to finish and see output in real-time
                # subprocess.run with no capture_output lets it print to stdout/stderr directly
                result = subprocess.run(cmd)
                
                exit_code = result.returncode
                if exit_code != 0:
                    print(f"[Loop] WARNING: run.py exited with code {exit_code}")
                
            except KeyboardInterrupt:
                # If user hits Ctrl+C during run.py, subprocess catches it? 
                # Usually python propagates it. We should handle it gracefully to stop the loop.
                raise KeyboardInterrupt
            except Exception as e:
                print(f"[Loop] Error executing run.py: {e}")
            
            # 3. Delay
            if loop_count == -1 or iteration < loop_count:
                print(f"[Loop] Sleeping for {delay} seconds...")
                time.sleep(delay)
                
    except KeyboardInterrupt:
        print("\n\n[Loop] Interrupted by user. Exiting...")
    
    print("="*60)
    print("[Loop] Batch Execution Finished.")

if __name__ == "__main__":
    main()
