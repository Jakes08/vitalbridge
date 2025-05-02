import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';

export default function Dashboard() {
    const { currentUser } = useAuth();
    const [activeTab, setActiveTab] = useState('profile');

    const ProfileSection = () => (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-4">Profile Information</h3>
            <div className="space-y-4">
                <div>
                    <label className="block text-gray-700">Email</label>
                    <p className="font-medium">{currentUser?.email}</p>
                </div>
                <div>
                    <label className="block text-gray-700">Last Sign In</label>
                    <p className="font-medium">{currentUser?.metadata?.lastSignInTime}</p>
                </div>
            </div>
        </div>
    );

    const SettingsSection = () => (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-4">Account Settings</h3>
            <div className="space-y-4">
                <div className="flex items-center justify-between">
                    <span>Email Notifications</span>
                    <input type="checkbox" className="form-checkbox" />
                </div>
                <div className="flex items-center justify-between">
                    <span>Dark Mode</span>
                    <input type="checkbox" className="form-checkbox" />
                </div>
            </div>
        </div>
    );

    return (
        <div className="p-8">
            <h2 className="text-2xl font-bold mb-6 text-center">
                Welcome, {currentUser?.email || 'Guest'}!
            </h2>
            
            <div className="flex space-x-4 mb-6">
                <button 
                    className={`px-4 py-2 rounded ${activeTab === 'profile' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
                    onClick={() => setActiveTab('profile')}
                >
                    Profile
                </button>
                <button 
                    className={`px-4 py-2 rounded ${activeTab === 'settings' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
                    onClick={() => setActiveTab('settings')}
                >
                    Settings
                </button>
            </div>

            <div className="max-w-2xl mx-auto">
                {activeTab === 'profile' ? <ProfileSection /> : <SettingsSection />}
            </div>
        </div>
    );
}