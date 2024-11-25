$(document).ready(function() {
    // Toggle item details when clicking on a row
    $('.item-row').click(function() {
        const itemId = $(this).data('item-id');
        const detailsRow = $(`#details-${itemId}`);
        
        // Hide all other detail rows
        $('.item-details').not(detailsRow).addClass('d-none');
        
        // Toggle current detail row
        detailsRow.toggleClass('d-none');
    });

    // Initialize tooltips
    $('[data-toggle="tooltip"]').tooltip();

    // Add click handler for filter button
    $('.btn-outline-primary').click(function() {
        // Add filter functionality here
        console.log('Filter clicked');
    });

    // Add click handler for order stock button
    $('.btn-primary').click(function() {
        // Add order stock functionality here
        console.log('Order stock clicked');
    });

    // Close details when clicking outside
    $(document).click(function(e) {
        if (!$(e.target).closest('.item-row, .item-details').length) {
            $('.item-details').addClass('d-none');
        }
    });
});