import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import translationEN from './locales/en/translation.json';
import translationSW from './locales/sw/translation.json';

const resources = {
    en: { translation: translationEN },
    sw: { translation: translationSW },
};

i18n.use(initReactI18next).init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: { escapeValue: false },
});

export default i18n;
// This file is responsible for setting up the i18next internationalization library.
// It imports the i18next library and the react-i18next module for React integration.
// It also imports translation files for English and Swahili languages.
// The resources object contains the translations for each language.
// The i18n instance is configured with the resources, default language (English), and fallback language (English).
// The escapeValue option is set to false to prevent escaping of HTML characters in translations.
// Finally, the i18n instance is exported for use in the application.
// The translation files are expected to be in JSON format and located in the specified paths.
// The i18next library is a powerful internationalization framework for JavaScript applications.
// It provides a simple and flexible way to manage translations and supports features like pluralization, interpolation, and context.