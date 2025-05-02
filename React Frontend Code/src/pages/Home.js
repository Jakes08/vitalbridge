import React from 'react';
import { useTranslation } from 'react-i18next';
import logo from '../assets/logo.png'; // Place your logo in src/assets

export default function Home() {
    const { t, i18n } = useTranslation();

    const switchLang = (lang) => {
        i18n.changeLanguage(lang);
    };

    return (
        <div className="p-8 text-center">
            <img src={logo} alt="VitalBridge Logo" className="mx-auto w-32 mb-4 animate-pulse" />
            <h1 className="text-5xl font-extrabold mb-4 animate-fadeIn">{t('welcome')}</h1>
            <p className="text-xl italic mb-8">Connecting Health, Anytime, Anywhere</p>
            <div>
                <button onClick={() => switchLang('en')} className="m-2 px-4 py-2 bg-blue-500 text-white rounded">English</button>
                <button onClick={() => switchLang('sw')} className="m-2 px-4 py-2 bg-green-500 text-white rounded">Swahili</button>
            </div>
        </div>
    );
}
// This code defines a React functional component called Home.
// It uses the useTranslation hook from the react-i18next library to handle internationalization.
// The component renders a home page with a logo, a welcome message, and a tagline.
// It also includes buttons to switch between English and Swahili languages.
// The switchLang function is called when the buttons are clicked, changing the language using the i18n.changeLanguage method.
// The logo is imported from the assets folder, and the text is styled using Tailwind CSS classes.
// The component is exported as the default export, making it available for use in other parts of the application.
// The useTranslation hook provides the t function for translating text based on the current language.
// The component is styled with Tailwind CSS classes for a modern and responsive design.
// The logo is animated with a pulse effect, and the welcome message has a fade-in animation.