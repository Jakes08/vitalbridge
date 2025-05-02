import React from 'react';

export default function Footer() {
    return (
        <footer className="bg-gray-200 text-center py-6 mt-auto border-t border-gray-300">
            <div className="container mx-auto">
                <p className="text-gray-600 text-sm">
                    &copy; {new Date().getFullYear()} VitalBridge. All rights reserved.
                </p>
                <nav className="mt-2">
                    <a href="/privacy" className="text-sm text-gray-600 hover:text-gray-800 mx-2">
                        Privacy Policy
                    </a>
                    <a href="/terms" className="text-sm text-gray-600 hover:text-gray-800 mx-2">
                        Terms of Service
                    </a>
                </nav>
            </div>
        </footer>
    );
}
//             {activeTab === 'profile' ? <ProfileSection /> : <SettingsSection />}
//         </div>
//     );
// }
// // This code defines a React functional component called Dashboard.
// // It uses the useState hook to manage the active tab state.
// // The component imports the useAuth hook to access the current user's authentication state.
// // It defines two sections: ProfileSection and SettingsSection, which display user information and account settings respectively.
// // The ProfileSection shows the user's email and last sign-in time, while the SettingsSection allows toggling email notifications and dark mode.
// // The component renders a welcome message with the user's email and buttons to switch between the profile and settings tabs.
// // The active tab is highlighted with a different background color.
// // The component is styled using Tailwind CSS classes for a clean and modern look.
// // The ProfileSection and SettingsSection components are conditionally rendered based on the active tab state.