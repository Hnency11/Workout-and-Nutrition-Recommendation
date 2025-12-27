import React, { useState } from 'react';
import axios from 'axios';
import { motion, AnimatePresence } from 'framer-motion';
import { Activity, Salad, Target, Clock, Zap, ArrowRight, RefreshCw } from 'lucide-react';

const API_URL = 'http://localhost:8000';

function App() {
    const [profile, setProfile] = useState({
        difficulty: 3,
        duration: 30,
        intensity: 3,
        goal: 0
    });

    const [recommendations, setRecommendations] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await axios.post(`${API_URL}/recommend`, profile);
            setRecommendations(response.data);
        } catch (error) {
            console.error("Error fetching recommendations:", error);
            alert("Make sure the backend is running!");
        } finally {
            setLoading(false);
        }
    };

    const renderRecommendationCard = (item, type) => (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="glass-card"
            key={item.name}
        >
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1rem' }}>
                <div style={{ padding: '0.8rem', background: 'rgba(99, 102, 241, 0.1)', borderRadius: '12px' }}>
                    {type === 'workout' ? <Activity className="text-primary" /> : <Salad className="text-secondary" />}
                </div>
                <h3 style={{ fontSize: '1.25rem' }}>{item.name}</h3>
            </div>
            <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem', lineHeight: '1.6' }}>{item.description}</p>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                {type === 'workout' ? (
                    <>
                        <div className="stat-item">
                            <span className="label">Difficulty</span>
                            <p>{item.difficulty}/5</p>
                        </div>
                        <div className="stat-item">
                            <span className="label">Duration</span>
                            <p>{item.duration} min</p>
                        </div>
                    </>
                ) : (
                    <>
                        <div className="stat-item">
                            <span className="label">Calories</span>
                            <p>{item.calories} kcal</p>
                        </div>
                        <div className="stat-item">
                            <span className="label">Protein</span>
                            <p>{item.protein}g</p>
                        </div>
                    </>
                )}
            </div>
        </motion.div>
    );

    return (
        <div className="app-container">
            <header style={{ textAlign: 'center', marginBottom: '4rem' }}>
                <motion.h1
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                >
                    Personalized Fitness AI
                </motion.h1>
                <p style={{ color: 'var(--text-muted)' }}>Get custom workout and nutrition plans powered by machine learning.</p>
            </header>

            <main>
                {!recommendations ? (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="glass-card"
                        style={{ maxWidth: '600px', margin: '0 auto' }}
                    >
                        <h2 style={{ marginBottom: '2rem' }}>Configure Your Profile</h2>
                        <form onSubmit={handleSubmit}>
                            <div style={{ marginBottom: '1.5rem' }}>
                                <label className="label">Fitness Goal</label>
                                <select
                                    value={profile.goal}
                                    onChange={(e) => setProfile({ ...profile, goal: parseInt(e.target.value) })}
                                >
                                    <option value={0}>Weight Loss</option>
                                    <option value={1}>Muscle Gain</option>
                                    <option value={2}>Flexibility & Maintenance</option>
                                </select>
                            </div>

                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                                <div>
                                    <label className="label">Desired Difficulty (1-5)</label>
                                    <input
                                        type="number" min="1" max="5"
                                        value={profile.difficulty}
                                        onChange={(e) => setProfile({ ...profile, difficulty: parseInt(e.target.value) })}
                                    />
                                </div>
                                <div>
                                    <label className="label">Workout Duration (min)</label>
                                    <input
                                        type="number" min="15" max="90"
                                        value={profile.duration}
                                        onChange={(e) => setProfile({ ...profile, duration: parseInt(e.target.value) })}
                                    />
                                </div>
                            </div>

                            <div style={{ marginBottom: '2rem' }}>
                                <label className="label">Exercise Intensity (1-5)</label>
                                <input
                                    type="number" min="1" max="5"
                                    value={profile.intensity}
                                    onChange={(e) => setProfile({ ...profile, intensity: parseInt(e.target.value) })}
                                />
                            </div>

                            <button type="submit" className="btn btn-primary" style={{ width: '100%' }} disabled={loading}>
                                {loading ? <RefreshCw className="animate-spin" /> : <>Get Recommendations <ArrowRight size={18} /></>}
                            </button>
                        </form>
                    </motion.div>
                ) : (
                    <div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
                            <h2 style={{ fontSize: '2rem' }}>Your Recommendations</h2>
                            <button onClick={() => setRecommendations(null)} className="btn" style={{ background: 'rgba(255,255,255,0.05)' }}>
                                Reset Profile
                            </button>
                        </div>

                        <section style={{ marginBottom: '4rem' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
                                <Zap className="text-accent" />
                                <h3 style={{ fontSize: '1.5rem' }}>Workout Plans</h3>
                            </div>
                            <div className="grid-layout">
                                {recommendations.workouts.map(w => renderRecommendationCard(w, 'workout'))}
                            </div>
                        </section>

                        <section>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
                                <Salad className="text-success" />
                                <h3 style={{ fontSize: '1.5rem' }}>Nutrition Guide</h3>
                            </div>
                            <div className="grid-layout">
                                {recommendations.nutrition.map(n => renderRecommendationCard(n, 'nutrition'))}
                            </div>
                        </section>
                    </div>
                )}
            </main>
        </div>
    );
}

export default App;
