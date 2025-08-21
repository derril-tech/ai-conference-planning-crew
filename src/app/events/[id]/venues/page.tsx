import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { mockVenues } from '@/lib/mock-data'

export default function EventVenuesPage({ params }: { params: { id: string } }) {
  return (
    <div>
      {/* Page Header */}
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Venues</h1>
          <p className="text-gray-600 mt-2">Manage venue shortlist and negotiations</p>
        </div>
        <Button className="bg-conference-600 hover:bg-conference-700">
          Add Venue
        </Button>
      </div>

      {/* Venue Cards */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {mockVenues.map((venue) => (
          <Card key={venue.id} className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <div className="flex justify-between items-start">
                <div>
                  <CardTitle className="text-xl">{venue.name}</CardTitle>
                  <CardDescription className="mt-1">
                    {venue.address}
                  </CardDescription>
                </div>
                <span className="status-chip status-success">Selected</span>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {/* Capacity and Rooms */}
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <span className="text-sm font-medium text-gray-700">Capacity</span>
                    <p className="text-lg font-semibold">{venue.capacity.toLocaleString()}</p>
                  </div>
                  <div>
                    <span className="text-sm font-medium text-gray-700">Rooms</span>
                    <p className="text-lg font-semibold">{venue.rooms.length}</p>
                  </div>
                </div>

                {/* Cost Summary */}
                <div>
                  <span className="text-sm font-medium text-gray-700">Total Cost</span>
                  <p className="text-2xl font-bold text-conference-600">
                    ${venue.costCards[0]?.total.toLocaleString()}
                  </p>
                </div>

                {/* Amenities */}
                <div>
                  <span className="text-sm font-medium text-gray-700">Amenities</span>
                  <div className="flex flex-wrap gap-2 mt-1">
                    {venue.amenities.map((amenity, index) => (
                      <span 
                        key={index}
                        className="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded-full"
                      >
                        {amenity}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Contact Info */}
                <div className="border-t pt-4">
                  <span className="text-sm font-medium text-gray-700">Contact</span>
                  <p className="text-sm text-gray-600 mt-1">
                    {venue.contactInfo.name} • {venue.contactInfo.email}
                  </p>
                </div>

                {/* Actions */}
                <div className="flex gap-2 pt-4">
                  <Button variant="outline" className="flex-1">
                    View Details
                  </Button>
                  <Button variant="outline" className="flex-1">
                    Edit Contract
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Empty State */}
      {mockVenues.length === 0 && (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-conference-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <span className="text-conference-600 text-2xl">🏢</span>
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">No venues yet</h3>
          <p className="text-gray-600 mb-6">Start by adding venues to your shortlist.</p>
          <Button className="bg-conference-600 hover:bg-conference-700">
            Add First Venue
          </Button>
        </div>
      )}
    </div>
  )
}
