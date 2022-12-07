import create from "zustand";

export const useAppStore = create( set => ({
    persons: [],
    setPersons: persons => set(state => ({
        ...state,
        persons
    })),
}));