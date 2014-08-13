
# $Id: smeserver-wbl.spec,v 1.7 2014/04/11 20:03:52 stephdl Exp $
# Authority: gzartman
# Name: Greg Zartman

Summary: E-mail white/black lists for SME Server
%define name smeserver-wbl
Name: %{name}
%define version 0.1.0
%define release 20
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: SME Server/addon
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.13.1-03
Requires: smeserver-release => 8.0
AutoReqProv: no

%description
%name is an addon for SME Server that provides the following WBLs:
qpsmtpd check_badmailfrom /var/qmail/control/badmailfrom
qpsmtpd check_spamhelo /var/service/qpsmtpd/config/badhelo
qpsmtpd whitelist_soft /var/service/qpsmtpd/config/whitelisthosts whitelisthelo whitelistsenders
spamassassin /etc/mail/spammassassin/local.cf whitelist_from

%changelog
* Tue Apr 8 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-20.sme
- patch to rename variables which have earlier declarations in the same scope. [SME: 8319]
- add a new usage legend for whitelistsenders by john crisp [SME: 8321]

* Mon Jul 15 2013 JP Pialasse <tests@pialasse.com> 0.1.0-19.sme
- apply locale 2013-07-15 patch
- fix for SME8 [SME: 7007]
- fix badmailfrom ignored by qpsmtpd, but without regex support [SME: 5085] 

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 0.1.0-18.sme
- apply locale 2011-03-06 patch

* Sun May 23 2010 SME Translation Server <translations@contribs.org> 0.1.0-17.sme
- apply locale 2010-05-23 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 0.1.0-16.sme
- apply locale 2010-03-02 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 0.1.0-15.sme
- apply locale 2009-10-27 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 0.1.0-14.sme
- apply locale 2009-08-24 patch

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 0.1.0-13.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 0.1.0-12.sme
- apply locale 2009-04-27 patch

* Tue Mar 03 2009 SME Translation Server
- apply locale 2009-03-03 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-10
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-9
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Wed Nov 19 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-8
- Apply 19 Nov 2008 locale patch

* Mon Nov 10 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-7
- Apply 10 Nov 2008 locale patch

* Fri Nov  7 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-6
- Apply  7 Nov 2008 locale patch

* Thu Nov  6 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-5
- Apply  6 Nov 2008 locale patch

* Fri Oct 17 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-4
- Apply 17 Oct 2008 locale patch

* Thu Oct 16 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-3
- Apply 16 Oct 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.1.0-2
- Apply 14 Oct 2008 locale patch

* Mon Oct 13 2008 Shad L. Lords <slords@mail.com> 0.1.0-1.sme
- Roll new stream to import into buildsys

* Fri Oct 10 2008 Greg J. Zartman <greg@leiinc.com> 0.0.1-9
- Add whitelist_soft qpsmtpd plugin template fragment for external connections.
- Simplify server-manager panel.

* Fri Jan 05 2007 Darrell May <dmay@myezserver.com>
- added spamassassin whitelist_from to accept panel
- reworked all code to use spamassassin db format
- [0.0.1-a8.dmay]

* Thu Jan 04 2007 Darrell May <dmay@myezserver.com>
- edited panels, added Update panel
- [0.0.1-a7.dmay]

* Thu Jan 04 2007 Darrell May <dmay@myezserver.com>
- edited templates to use new db
- added templates for spamassassin local.cf whitelist_from
- [0.0.1-a6.dmay]

* Wed Jan 03 2007 Darrell May <dmay@myezserver.com>
- changed db to use /home/e-smith/db/wbl
- [0.0.1-a5.dmay]

* Sun Dec 17 2006 Darrell May <dmay@myezserver.com>
- initial public alpha release
- [0.0.1-a4.dmay]

* Sat Dec 16 2006 Darrell May <dmay@myezserver.com>
- more panel enhancements
- [0.0.1-a3.dmay]

* Fri Dec 15 2006 Darrell May <dmay@myezserver.com>
- continued panel enhancements
- [0.0.1-a2.dmay]

* Fri Dec 15 2006 Darrell May <dmay@myezserver.com>
- server-manager panel added
- [0.0.1-a1.dmay]

* Fri Dec 15 2006 Darrell May <dmay@myezserver.com>
- initial alpha release
- [0.0.1-a0.dmay]

%prep
%setup
%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc " >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

