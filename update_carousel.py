import re

with open('resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new section
new_section = """    <!-- III. Articles Section -->
    <section class="services-section section-padding" style="background-color: var(--bg-white);">
        <div class="container reveal" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px;">
            <div>
                <h2 class="section-title">Blog and Articles</h2>
                <div class="divider-terracotta"></div>
                <p class="section-subtitle">Read the latest insights on change and leadership.</p>
            </div>
            <!-- Navigation arrows -->
            <div class="carousel-nav" style="display: flex; gap: 10px; margin-bottom: 20px;">
                <button id="blog-prev" class="btn btn-outline" style="width: 44px; height: 44px; border-radius: 50%; padding: 0; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s ease;"><i class="fa-solid fa-chevron-left"></i></button>
                <button id="blog-next" class="btn btn-outline" style="width: 44px; height: 44px; border-radius: 50%; padding: 0; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s ease;"><i class="fa-solid fa-chevron-right"></i></button>
            </div>
        </div>
        <div class="container reveal">
            <style>
                #blog-carousel::-webkit-scrollbar {
                    display: none;
                }
                .blog-card-carousel {
                    flex: 0 0 calc(33.333% - 20px);
                    min-width: 320px;
                    scroll-snap-align: start;
                    background: #f5f5f7;
                    height: auto;
                    padding: 0;
                    display: flex;
                    flex-direction: column;
                    justify-content: flex-start;
                    text-decoration: none;
                }
                @media (max-width: 992px) {
                    .blog-card-carousel {
                        flex: 0 0 calc(50% - 15px);
                    }
                }
                @media (max-width: 768px) {
                    .blog-card-carousel {
                        flex: 0 0 100%;
                    }
                }
            </style>
            <div id="blog-carousel" style="display: flex; gap: 30px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 20px; scrollbar-width: none; -ms-overflow-style: none; scroll-behavior: smooth;">
                <!-- Article 1 -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">I Spent 15 Years Studying Why Change Fails Here's What I Found</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">Are you where you hoped to be at this point in your life? If not, why? That's the question I ask audiences...</p>
                        <a href="https://tonychatman.com/i-spent-15-years-studying-why-change-fails-heres-what-i-found/" target="_blank" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>
                
                <!-- Article 2 -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">You're Not Hiring Bad People, You're Making Bad People</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">I've heard the conversation a hundred times. I can't tell you how it starts, but at somepoint, a manager...</p>
                        <a href="https://tonychatman.com/youre-not-hiring-bad-people-youre-making-bad-people/" target="_blank" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>

                <!-- Article 3 -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1529156069898-49953eb1f5f6?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">When It Comes To Bad Managers, I Say Blame The Parents</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">We've all seen it, whether at a mall, a playground, our kid's school or even whilevisiting family, we've...</p>
                        <a href="https://tonychatman.com/when-it-comes-to-bad-managers-i-say-blame-the-parents/" target="_blank" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>
                
                <!-- Article 4 (Dummy) -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1552581234-26160f608093?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">The Anatomy of a High-Performing Team</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">Building a team that performs under pressure doesn't happen by accident. Here are the 5 pillars of team success...</p>
                        <a href="#" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>
                
                <!-- Article 5 (Dummy) -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">Navigating Corporate Change Without Losing Your Mind</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">Change is inevitable, but burnout isn't. Discover how top executives guide their organizations through transitions.</p>
                        <a href="#" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>
                
                <!-- Article 6 (Dummy) -->
                <div class="service-card blog-card-carousel">
                    <div style="height: 220px; width: 100%; background-image: url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=60'); background-size: cover; background-position: center; border-radius: 24px 24px 0 0;"></div>
                    <div style="padding: 35px; display: flex; flex-direction: column; flex-grow: 1; color: var(--text-color);">
                        <h3 style="font-size: 21px; margin-bottom: 15px; color: var(--text-color); font-weight: 600; letter-spacing: -0.01em; line-height: 1.3;">Why Empathy is Your Greatest Leadership Asset</h3>
                        <p style="font-size: 15px; color: var(--text-color-secondary); margin-bottom: 25px; line-height: 1.5; flex-grow: 1;">The best leaders aren't just strategists; they're empathetic listeners. Learn how to cultivate empathy in leadership.</p>
                        <a href="#" class="btn btn-outline" style="align-self: flex-start; font-size: 14px; padding: 8px 18px;">Read More</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const carousel = document.getElementById('blog-carousel');
            const prevBtn = document.getElementById('blog-prev');
            const nextBtn = document.getElementById('blog-next');
            
            if (carousel && prevBtn && nextBtn) {
                // Calculate scroll amount based on card width + gap
                const getScrollAmount = () => {
                    const card = carousel.querySelector('.blog-card-carousel');
                    if (card) {
                        return card.offsetWidth + 30; // 30 is the gap
                    }
                    return 350; // Fallback
                };

                prevBtn.addEventListener('click', () => {
                    carousel.scrollBy({ left: -getScrollAmount(), behavior: 'smooth' });
                });
                
                nextBtn.addEventListener('click', () => {
                    carousel.scrollBy({ left: getScrollAmount(), behavior: 'smooth' });
                });
            }
        });
    </script>
"""

# Regex to find the existing section
pattern = r'<!-- III\. Articles Section -->.*?</section>'
content = re.sub(pattern, new_section, content, flags=re.DOTALL)

with open('resources.html', 'w', encoding='utf-8') as f:
    f.write(content)
