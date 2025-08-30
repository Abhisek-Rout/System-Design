# Momento Pattern
## Problem statement:
How to provide undo/redo functionality or state restoration without exposing the object's internal state and breaking encapsualation

## Solution
The momento pattern captures the internal state of an object in a momento, allowing the object to restore its state later or without revealing internal details

## Components of Momento Pattern
1. Originator: The object whose state needs to be saved and restored (e.g Text_Editor)
2. Momento: Captures and stores the internal state of the originator (e.g Editor_Momento)
3. Caretaker: Manages and stores the moementos, without modifying them.

## Use-cases
1. *Undo/Redo in Applications*: Commonly used in text editors, drawing applications or any system that requires history management.

2. *State Restoration*: Used in scenarios where you need to periodically save system states (e.g games, data recovery) and allow users to return to previous states.

## Examples:
1. *Games*: Saving the game state for load/reload functionality.
2. *Document Editor*: Undo/redo functionality to navigate through document changes.