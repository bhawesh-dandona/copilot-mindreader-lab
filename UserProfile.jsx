import { useState } from 'react';

export default function UserProfile() {
  const [showBio, setShowBio] = useState(false);

  const user = {
    name: 'Alex Morgan',
    email: 'alex.morgan@example.com',
    bio: 'A curious learner who enjoys building thoughtful, user-friendly experiences.',
  };

  return (
    <article className="user-profile">
      <h2>{user.name}</h2>
      <p>
        <a href={`mailto:${user.email}`}>{user.email}</a>
      </p>
      <button
        type="button"
        aria-expanded={showBio}
        onClick={() => setShowBio((visible) => !visible)}
      >
        {showBio ? 'Hide bio' : 'Show bio'}
      </button>
      {showBio && <p>{user.bio}</p>}
    </article>
  );
}