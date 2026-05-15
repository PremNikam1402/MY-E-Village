from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer


class CourseListView(APIView):
    """GET /api/education/courses/ — Browse all courses"""

    def get(self, request):
        courses = Course.objects.filter(is_active=True)
        serializer = CourseSerializer(courses, many=True, context={'request': request})
        return Response(serializer.data)


class EnrollView(APIView):
    """POST /api/education/enroll/ — Enroll in a course"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        course_id = request.data.get('course')
        try:
            course = Course.objects.get(id=course_id, is_active=True)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)

        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user, course=course
        )
        if not created:
            return Response({'message': 'Already enrolled'})
        return Response(EnrollmentSerializer(enrollment).data, status=status.HTTP_201_CREATED)