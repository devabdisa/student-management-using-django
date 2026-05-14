# Render Deployment Checklist

## Pre-Deployment ✅
- [x] PostgreSQL database created on Render
- [x] Environment variables configured
- [x] psycopg2-binary added to requirements.txt
- [x] gunicorn added to requirements.txt
- [x] Procfile configured correctly
- [x] build.sh script created
- [x] smart_migrate command handles migration conflicts
- [x] Demo data seeding script ready
- [x] Changes committed and pushed to GitHub

## During Deployment (Monitor These)
- [ ] Render detects new commit
- [ ] Build starts automatically
- [ ] Dependencies install successfully
- [ ] psycopg2-binary installs without errors
- [ ] gunicorn installs without errors
- [ ] Static files collected
- [ ] smart_migrate runs successfully
- [ ] Guardian and StudentGuardian tables created
- [ ] Initial admin user created
- [ ] Demo data seeded
- [ ] Build completes successfully
- [ ] Service starts and becomes live

## Post-Deployment Testing
- [ ] Application URL is accessible
- [ ] Login page loads correctly
- [ ] Test admin login (admin1@school.com / admin123)
- [ ] Admin dashboard displays correctly
- [ ] Test teacher login (teacher1@school.com / teacher123)
- [ ] Test student login (student1@school.com / student123)
- [ ] Test parent login (parent1@school.com / parent123)
- [ ] Navigate to Manage Staff page
- [ ] Click "View" button on a staff member
- [ ] Navigate to Manage Students page
- [ ] Click "View" button on a student
- [ ] Verify guardian information displays for students
- [ ] Check that all static files (CSS, JS, images) load
- [ ] Test timetable functionality
- [ ] Verify no notification/leave menu items appear

## Common Issues & Solutions

### Issue: psycopg2 still fails
**Solution**: Check if psycopg2-binary is spelled correctly in requirements.txt

### Issue: Migration conflicts
**Solution**: smart_migrate command should handle this automatically

### Issue: Static files not loading
**Solution**: 
- Verify STATIC_ROOT in settings.py
- Check whitenoise configuration
- Ensure collectstatic ran in build.sh

### Issue: 500 Internal Server Error
**Solution**:
- Check Render logs for detailed error
- Verify all environment variables are set
- Check DATABASE_URL is correct

### Issue: Demo data not seeded
**Solution**:
- Check if seed_demo_data command ran in build logs
- Verify no errors in the seeding process
- May need to run manually: `python manage.py seed_demo_data`

## Render Dashboard Links
- **Deployments**: https://dashboard.render.com/
- **Logs**: Check "Logs" tab in your service
- **Environment**: Check "Environment" tab for variables
- **Events**: Check "Events" tab for deployment history

## Database Connection Test
If deployment succeeds but database issues persist:
```bash
# Connect to Render shell
# Run Django shell
python manage.py shell

# Test database connection
from django.db import connection
connection.ensure_connection()
print("Database connected!")

# Check if tables exist
from main_app.models import Guardian, StudentGuardian
print(Guardian.objects.count())
print(StudentGuardian.objects.count())
```

## Rollback Plan
If deployment fails completely:
1. Check previous working commit
2. Revert to that commit: `git revert HEAD`
3. Push to trigger new deployment
4. Investigate issue locally before redeploying

## Success Criteria
✅ Build completes without errors  
✅ All migrations run successfully  
✅ Demo accounts can login  
✅ All pages load correctly  
✅ View buttons work for staff and students  
✅ No 500 errors in logs  
✅ Static files load properly  

---
**Last Updated**: May 13, 2026  
**Status**: Awaiting deployment after psycopg2-binary fix
