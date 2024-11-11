document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('countrySelect');
    const conditionsDisplay = document.getElementById('conditionsDisplay');

    // Fetch available countries
    fetch('/api/countries')
        .then(response => response.json())
        .then(countries => {
            // Sort countries alphabetically
            countries.sort().forEach(country => {
                const option = document.createElement('option');
                option.value = country;
                option.textContent = country;
                countrySelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching countries:', error);
            conditionsDisplay.innerHTML = '<p class="error">Error loading countries. Please try again later.</p>';
        });

    // Handle country selection
    countrySelect.addEventListener('change', function() {
        const selectedCountry = this.value;
        if (selectedCountry) {
            conditionsDisplay.innerHTML = '<p class="loading">Loading conditions...</p>';
            fetch(`/api/conditions/${selectedCountry}`)
                .then(response => response.json())
                .then(conditions => {
                    if (Object.keys(conditions).length === 0) {
                        conditionsDisplay.innerHTML = '<p class="error">No conditions found for this country.</p>';
                        return;
                    }
                    displayConditions(conditions, selectedCountry);
                })
                .catch(error => {
                    console.error('Error fetching conditions:', error);
                    conditionsDisplay.innerHTML = '<p class="error">Error loading conditions. Please try again later.</p>';
                });
        } else {
            conditionsDisplay.innerHTML = '';
        }
    });

    function displayConditions(conditions, country) {
        let html = `
            <h2><i class="fas fa-globe-asia"></i> ${country} - Mango Import Conditions</h2>
            <div class="condition-section">
                <h3><i class="fas fa-file-contract"></i> Required Permits</h3>
                <ul>
                    ${conditions.permits_required.map(permit => `<li>${permit}</li>`).join('')}
                </ul>
            </div>
            <div class="condition-section">
                <h3><i class="fas fa-flask"></i> Required Treatments</h3>
                <ul>
                    ${conditions.treatments.map(treatment => `<li>${treatment}</li>`).join('')}
                </ul>
            </div>
            <div class="condition-section">
                <h3><i class="fas fa-file-alt"></i> Required Documentation</h3>
                <ul>
                    ${conditions.documentation.map(doc => `<li>${doc}</li>`).join('')}
                </ul>
            </div>
            <div class="condition-section">
                <h3><i class="fas fa-clipboard-check"></i> Additional Requirements</h3>
                <ul>
                    ${conditions.additional_requirements.map(req => `<li>${req}</li>`).join('')}
                </ul>
            </div>
            <div class="condition-section">
                <h3><i class="fas fa-info-circle"></i> Detailed Conditions</h3>
                <p>${conditions.detailed_conditions}</p>
            </div>
            <div class="bicon-link">
                <a href="${conditions.bicon_link}" target="_blank">
                    <i class="fas fa-external-link-alt"></i> View Full BICON Details
                </a>
            </div>
        `;
        conditionsDisplay.innerHTML = html;
    }
});
