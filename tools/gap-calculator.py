#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# EMERATH Gap Calculator v1.0
import argparse

def calculate_free_energy(survival, growth, impact=0, transcendence=0):
    return 10 * survival + 5 * growth + 0 * impact + 1 * transcendence

def main():
    parser = argparse.ArgumentParser(description="EMERATH Gap Calculator")
    parser.add_argument("--survival", type=int, required=True)
    parser.add_argument("--growth", type=int, required=True)
    parser.add_argument("--impact", type=int, default=0)
    parser.add_argument("--transcendence", type=int, default=0)
    args = parser.parse_args()
    
    F = calculate_free_energy(args.survival, args.growth, args.impact, args.transcendence)
    
    print(f"EMERATH Gap Calculator v1.0")
    print(f"===================================")
    print(f"Survival Gap: {args.survival} * 10")
    print(f"Growth Gap:   {args.growth} * 5")
    print(f"Impact Gap:   {args.impact} * 0")
    print(f"Transcendence Gap: {args.transcendence} * 1")
    print(f"")
    print(f"Free Energy (F) = {F}")
    print(f"===================================")
    print(f"")
    if F > 0:
        print(f"🚀 F > 0 → Driving! Action required.")
    else:
        print(f"⚠️  F = 0 → Warning: Don't lay flat!")

if __name__ == "__main__":
    main()
